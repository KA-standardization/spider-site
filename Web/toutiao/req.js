const http=require("https");

const url="https://www.toutiao.com/api/pc/list/feed?category=pc_user_hot&token=MS4wLjABAAAAAUpqv8LhlfYyfd0r-Pli7TQre1KET0HtOhycHrzzvx0&aid=24&app_name=toutiao_web";
http.get(url,{},(res)=>{
    console.log(res);
})