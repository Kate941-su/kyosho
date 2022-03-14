// ボタンクリックイベントが正しく届いているかテストする 
function testButtonClickEvent(){
    alert('javaScriptは正常に機能しています');
}

function OnFileSelect( inputElement )
{
    // ファイルリストを取得
    let fileList = inputElement.files;
    // ファイルの数を取得
    let fileCount = fileList.length;
    let loadCompleteCount = 0;
//    let imageList = "";
    // 選択されたファイルの数だけ処理する
    for ( let i = 0; i < fileCount; i++ ) {
        let fileReader = new FileReader();  // FileReaderを生成
        let file = fileList[ i ];   // ファイルを取得
        // 読み込み完了時の処理を追加
        fileReader.onload = function() {
            //アスペクト比を変えないように変更する
            // 選択時に画像を追加するときのコード
//            imageList += "<li><img src=\"" + this.result + "\" width=\"300\" height=\"300\" ></li>\r\n"; // <li>,<img>タグの生成
            // 選択されたファイルすべの処理が完了したら、<ul>タグに流し込む
            if ( ++loadCompleteCount == fileCount ) {
 //               document.getElementById("ID001").innerHTML = imageList;// <ul>タグに<li>,<img>を流し込む
                let srcimg = document.getElementById("srcImage");
                srcimg.src = this.result;
                let img = document.getElementById("filterImage");
                img.src = '/static/app/imgs/afterImage.png';
            }
        };
        // ファイルの読み込み(Data URI Schemeの取得)
        fileReader.readAsDataURL( file );
    }
    document.getElementById("btn_create").click();
    createWaitIndicator();
}

// 再加工時時の処理を行う
function onClickRecreate() {
    document.getElementById("btn_recreate").click();
    createWaitIndicator();
}

// ウェイトインジケータを作成する
function createWaitIndicator() {
    // ウェイトインジケーター親要素取得
    let waitIndicator = document.getElementById("waitIndicator");
    // ウェイトインジケーター子要素取得
    let childElement = document.createElement("div");
    // 属性設定
    childElement.setAttribute("class", "loader");
    // 親要素に追加
    waitIndicator.insertBefore(childElement, waitIndicator.firstChild);
}

/*
let button_threshold = document.getElementById('btn_threshold');
let button_mosaic = document.getElementById('btn_mosaic');
let button_subColor = document.getElementById('btn_subColor');
let button_dotArt = document.getElementById('btn_dotArt');
button_threshold.addEventListener('click', testButtonClickEvent);
button_mosaic.addEventListener('click', testButtonClickEvent);
button_subColor.addEventListener('click', testButtonClickEvent);
button_dotArt.addEventListener('click', testButtonClickEvent);
*/