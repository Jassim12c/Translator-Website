const sentenceId = document.getElementById('id_sentence');
const innerP = document.getElementsByClassName('inner')[0];
sentenceId.addEventListener('input', displayLetters);

function displayLetters(){
    let sentenceValue = sentenceId.value;
    innerP.innerHTML = sentenceValue;
}
