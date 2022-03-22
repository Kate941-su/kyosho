const filterArray = ["dotArt", "mosaic", "threshold", "subColor", "gauss"]

// 初期画像配置時の処理
function onErrorFilterImage(obj){
    let srcImg = document.getElementById("srcImage");
    let dstImg = document.getElementById("dstImage");
    let wordList = obj.baseURI.split("/");
    const filterName = wordList[wordList.length - 2];
    srcImg.setAttribute("src", "/static/app/imgs/flower.jpg")
    if (filterName == filterArray[0]) { // ドット絵風のとき
        dstImg.setAttribute("src", "/static/app/imgs/flower_dotArt.jpg");        
    } else if (filterName == filterArray[1]) { // モザイクのとき
        dstImg.setAttribute("src", "/static/app/imgs/flower_mosaic.jpg");       
    } else if (filterName == filterArray[2]) { // 二値化のとき
        dstImg.setAttribute("src", "/static/app/imgs/flower_threshold.jpg");       
    } else if (filterName == filterArray[3]) { // 減色のとき
        dstImg.setAttribute("src", "/static/app/imgs/flower_subColor.jpg");       
    } else if (filterName == filterArray[4]) { // ガウスぼかしのとき
        dstImg.setAttribute("src", "/static/app/imgs/flower_gauss.jpg");       
    } else {
        console.assert(false, '%sは定義されていません。', filterName);
    }
    let downloadButton = document.getElementById("downloadButton");
    downloadButton.style.display="none";
};
