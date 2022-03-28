const express = require('express')
const decoder = new TextDecoder('gbk');
const child_process = require('child_process');
const fs = require('fs')
const path = require('path');
const app = express()

app.all('*', function (req, res, next) {
    res.header('Access-Control-Allow-Origin', '*');
    res.header('Access-Control-Allow-Headers', 'Content-Type, Content-Length, Authorization, Accept, X-Requested-With , yourHeaderFeild');
    res.header('Access-Control-Allow-Methods', 'PUT, POST, GET, DELETE, OPTIONS');
    if (req.method == 'OPTIONS') {
      res.send(200);
    } else {
      next();
    }
  });

app.use(express.static('file'))




app.get('/book', (req, res) => {
        console.log((req.query));
        const output = child_process.execSync('python '+path.join(__dirname,'./crawler/getWebBook.py'),{
            input:JSON.stringify(req.query),
            encoding:'utf-8',
            
        })
        res.status(200)
        // console.log(output);
        res.send(output)
        console.log('返回成功');
})

app.get('/content', (req, res) => {

    // console.log((req.query.bookname));
    console.log(req.url);
    const output = child_process.execSync('python '+path.join(__dirname,'./crawler/getBookContent.py'),{
        input:encodeURI(req.query.bookname),
        encoding:'utf8',
        
    })
    res.status(200)
    res.send(output)
    console.log(output);
    // console.log(output.toString());
    
})

app.get('/contentName',(req,res)=>{
    var contentNamePath = path.join(__dirname,'./contentName.txt')
    fs.readFile(contentNamePath,(err,data)=>{
        res.status(200)
        res.send(data)
    })
})






app.use((err, req, res, next) => {
    res.status(502)
    
    res.send(err)
})
app.listen(80, () => {
    console.log('webserve running as http://127.0.0.1:80');
})