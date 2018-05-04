const express = require('express')
const secure = require('express-force-https')
const path = require('path')
const serveStatic = require('serve-static')

const app = express()

app.use(serveStatic(path.join(__dirname, '/dist')))
app.use(secure)
app.get('*', function(req, res) {
  res.sendFile(path.join(__dirname, '/dist/index.html'))
})

let port = process.env.PORT || 5000
app.listen(port)

console.log('server started ' + port)
