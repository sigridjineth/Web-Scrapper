const axios = require("axios");
const cheerio = require("cheerio");
//const voca = require("voca")
const log = console.log;

const getHtml = async() => {
    var i=0
    while (i<493){
        try {
            return await axios.get("https://playentry.org/ds#!/qna?sort=created&rows=20&page=%d",i);
        } catch (error) {
            console.error(error);
        }
    }
};

getHtml()
    .then(html => {
        let ulList = [];
        var temp = new Array();
        const $ = cheerio.load(html.data);
        const $bodyList = $("div.discussContentWrapper div.discussListWrapper table.discussList").children("tr.discussRow");

        $bodyList.each(function(i, elem){
            ulList[i] = {
                title:$(this).find('td.discussTitle div.discussTitleWrapper'),
                writer:$(this).find('td.discussTitle td.discussViewCount'),
                viewcount:$(this).find('td.discussTitle td.discussViewCount'),
                likecount:$(this).find('td.discussTitle div.discussLikeCount'),
                date:$(this).find('td.discussTitle td.discussDate'),
            };
        });

    const data = ulList.filter(n => n.title);
    temp.push(data)
    
    return temp
})
.then(res => log(res));