const axios = require("axios");
const cheerio = require("cheerio");
const log = console.log;

const getHtml = async() => {
    try {
        return await axios.get("https://playentry.org/ds#!/qna?sort=created&rows=20&page=1");
    } catch (error) {
        console.error(error);
    }
};

getHtml()
    .then(html => {
        let ulList = [];
        const $ = cheerio.load(html.data);
        const $bodyList = $("div.global_header section.wrapper div.discussContentWrapper div.discussListWrapper table.discussList").children("tr.discussRow");

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
    return data;
})
.then(res => log(res));