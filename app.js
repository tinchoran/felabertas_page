const express = require("express");

const app = express()

const PORT = 3000

app.get("/", (req, res)=>{
    res.sendFile(__dirname + "/public/index.html")
})

app.get("/styles", (req, res)=>{
    res.send(__dirname + "/styles")
})

app.listen(PORT, ()=> console.log(`Servidor corriendo en el puerto: ${PORT}`))