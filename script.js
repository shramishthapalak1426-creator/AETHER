window.onload=function(){

if(localStorage.getItem("theme")==="dark"){
document.body.classList.add("dark")
}

}
let chart = null


function toggleTheme(){

document.body.classList.toggle("dark")

if(document.body.classList.contains("dark")){
localStorage.setItem("theme","dark")
}
else{
localStorage.setItem("theme","light")
}

}


/* YOUTUBE ANALYSIS */

function analyze(){

fetch("/analyze",{

method:"POST",

headers:{
"Content-Type":"application/x-www-form-urlencoded"
},

body:"url="+document.getElementById("url").value

})

.then(res=>res.json())

.then(data=>{

document.getElementById("result").innerText="Mood: "+data.mood
let total = data.positive + data.neutral + data.negative

let score = Math.round((data.positive / total) * 100)

document.getElementById("emotion-text").innerText =
"Positive Sentiment Score: " + score + "%"

document.getElementById("meter-fill").style.width = score + "%"

let ctx=document.getElementById("chart")

/* destroy old chart */

if(chart){
chart.destroy()
}

chart=new Chart(ctx,{
type:"pie",
data:{
labels:["Positive","Neutral","Negative"],
datasets:[{
data:[data.positive,data.neutral,data.negative],
backgroundColor:["#89CFF0","#D8B4FE","#F9A8D4"]
}]
},
options:{
responsive:true,
maintainAspectRatio:false
}
})


/* positive words */

let pos=document.getElementById("positive_words")
pos.innerHTML=""

data.top_positive.forEach(w=>{
let li=document.createElement("li")
li.innerText=w[0]+" : "+w[1]
pos.appendChild(li)
})


/* negative words */

let neg=document.getElementById("negative_words")
neg.innerHTML=""

data.top_negative.forEach(w=>{
let li=document.createElement("li")
li.innerText=w[0]+" : "+w[1]
neg.appendChild(li)
})


/* word cloud */

let cloud=[]

data.word_cloud.forEach(w=>{
cloud.push([w[0],w[1]*10])
})

WordCloud(document.getElementById("wordcloud"),{
list:cloud,
gridSize:10,
weightFactor:5
})

})

}


/* CHATBOT */

function chat(){

let message=document.getElementById("chat").value

if(message.trim()==="") return

let chatbox=document.getElementById("chatbox")

/* user bubble */

let user=document.createElement("div")
user.className="user-message"
user.innerText=message
chatbox.appendChild(user)


fetch("/chatbot",{

method:"POST",

headers:{
"Content-Type":"application/x-www-form-urlencoded"
},

body:"message="+message

})

.then(res=>res.json())

.then(data=>{

let bot=document.createElement("div")
bot.className="bot-message"
bot.innerText=data.response
chatbox.appendChild(bot)

chatbox.scrollTop=chatbox.scrollHeight

})

/* clear input */

document.getElementById("chat").value=""

}


/* ENTER KEY SEND */

function handleEnter(event){

if(event.key==="Enter"){
chat()
}

}


/* FEEDBACK */

function sendFeedback(){

let text=document.getElementById("feedback").value

fetch("/feedback",{

method:"POST",

headers:{
"Content-Type":"application/x-www-form-urlencoded"
},

body:"feedback="+text

})

.then(res=>res.json())

.then(data=>{

document.getElementById("feedback-msg").innerText =
"Thank you! Your feedback matters. Have a good day 😊"

document.getElementById("feedback").value=""

})

}