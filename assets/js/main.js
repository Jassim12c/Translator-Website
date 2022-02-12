const sentenceId = document.getElementById('id_sentence');
const innerP = document.getElementsByClassName('inner')[0];
const checkBox = document.getElementById('active');
const mainWrapper = document.getElementById('main-wrapper');
const title = document.getElementById("title");
const body = document.body;
const menuBtn = document.getElementsByClassName('menu-btn')[0];
//sentenceId.addEventListener('input', displayLetters());

/*
function displayLetters(){
    let sentenceValue = sentenceId.value;
    innerP.innerHTML = sentenceValue;
}
*/

function checkBoxCheck(){
    if(checkBox.checked == true){
        body.classList.add("diagonal-right");
        body.classList.add("body-color-transition");
        body.style.backgroundPosition = "center";
        menuBtn.style
    }else{
        body.classList.remove("diagonal-right");
        body.classList.remove("body-color-transition");
        body.style.backgroundPosition = "initial";
    }
}

menuBtn.addEventListener('click', ()=>{
    if(menuBtn.style.transform === ""){
        menuBtn.style.transform = "rotate(180deg)";
        menuBtn.style.color = "grey";
    }else{
        menuBtn.style.transform = "";
        menuBtn.style.color = "#A09D30";
    }
});
