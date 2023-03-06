
    let i = 1;
    for(let li of carousel.querySelectorAll('li')) {
    }


    let width = 400;
    let count = 1;

    let list = carousel.querySelector('ul');
    let listElems = carousel.querySelectorAll('li');

    let position = 0;

    carousel.querySelector('.prev').onclick = function() {



      position += width * count;

      position = Math.min(position, 0)
      list.style.marginLeft = position + 'px';
    };

    carousel.querySelector('.next').onclick = function() {



      position -= width * count;

      position = Math.max(position,  -width * 4);

      list.style.marginLeft = position + 'px';


    };