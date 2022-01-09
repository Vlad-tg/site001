window.onscroll = function() {scrollFunctionTwo()};

function scrollFunctionTwo() {
  if (document.body.scrollTop > 1 || document.documentElement.scrollTop > 1) {
    document.getElementById("line-nav-top-views-registration-id").style.background = "white";
    document.getElementById("line-nav-black-id").style.display = "none";
    document.getElementById("menu-svg").style.fill = "black";
    document.getElementById("top-div-all-a-about").style.color = "black";
    document.getElementById("top-div-all-a-contact").style.color = "black";
    document.getElementById("Layer_1").style.fill = "black";
    document.getElementById("span-id").style.color = "#000";
    document.getElementById("a-logout-views-id").style.color = "black";
    document.getElementById("top-div-all-a-hot").style.display = "none";
    document.getElementById("line-nav-top-views-registration-id").style.transition = "all 0.4s ease";
    document.getElementById("line-div").style.display = "block";
  }
  else {
    document.getElementById("line-nav-top-views-registration-id").style.background = "transparent";
    document.getElementById("line-nav-black-id").style.display = "block";
    document.getElementById("menu-svg").style.fill = "white";
    document.getElementById("Layer_1").style.fill = "#fff";
    document.getElementById("a-logout-views-id").style.color = "#fff";
    document.getElementById("span-id").style.color = "#fff";
    document.getElementById("top-div-all-a-about").style.color = "white";
    document.getElementById("top-div-all-a-contact").style.color = "white";
    document.getElementById("top-div-all-a-hot").style.display = "block";
    document.getElementById("line-div").style.display = "none";
  }
  if (document.body.scrollTop > 950 || document.documentElement.scrollTop > 950) {
    document.getElementById("block-two").style.opacity = "1";
    document.getElementById("block-two").style.transition = "all 3s ease";

  }
 if (document.body.scrollTop > 400 || document.documentElement.scrollTop > 400) {
    document.getElementById("block-one-id").style.opacity = "1";
    document.getElementById("block-one-id").style.transition = "all 1s ease";

  }
   if (document.body.scrollTop > 2550 || document.documentElement.scrollTop > 2550) {
    document.getElementById("block-three-id").style.opacity = "1";
    document.getElementById("block-three-id").style.transition = "all 1s ease";

  }
}