
const mouseTarget = document.getElementById('celebration');
const mouseTargetAdventure = document.getElementById('celebration adventure');
const unorderedList = document.getElementById('a-end-line-div');

mouseTarget.addEventListener('mouseover', e => {

  unorderedList.style.clip = 'rect(0px,80px,1px,0px)';

  unorderedList.style.transition = 'clip 1.5s';

});
 mouseTarget.addEventListener('mouseout', e => {
 unorderedList.style.clip = 'rect(0px,0px,0px,80px)';


});



