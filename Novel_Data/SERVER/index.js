var express = require('express')
var app = express()
var path = require('path')

app.use(express.static(path.join(__dirname, '../PUBLIC')))
app.use(express.static(path.join(__dirname, '../../Novel_Data')))
app.use(express.static(path.join(__dirname, 'NOVEL_BLURBS')))
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, '../PUBLIC/HTML/index.html'))
})

app.get('/archive', (req, res) => {
     res.sendFile(path.join(__dirname, '../PUBLIC/HTML/archive.html'))

})

app.listen(3000)