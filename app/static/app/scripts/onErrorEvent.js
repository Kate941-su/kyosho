function onErrorFilterImage(obj){
    let srcImg = document.getElementById("srcImage");
    let dstImg = document.getElementById("dstImage");
    srcImg.setAttribute("src", "/static/app/imgs/beforeImage.png")
    dstImg.setAttribute("src", "/static/app/imgs/afterImage.png")
};