let dstImage = document.getElementById("dstImage");
function onChangeDstImage() {
    // ウェイトインジケーター親要素取得
    let waitIndicator = document.getElementById("waitIndicator");
    // ウェイトインジケーター子要素取得
    let childElementLoader = document.getElementsByClassName("loader");
    let childElementModalWindow = document.getElementsByClassName("modalWindow");
    if (waitIndicator.hasChildNodes()) {
        waitIndicator.removeChild(childElementLoader);
        waitIndicator.removeChild(childElementModalWindow);
    }
}
/*動的画像変更監視
let mo = new MutationObserver(function() {
  alert('写真が変更されました。');
});
var config = {
//  childList: true,
  attributes: true,//「属性」の変化
//  characterData: true,//「テキストノード」の変化
//  subtree:true,
};
mo.observe(dstImage, config);
*/


