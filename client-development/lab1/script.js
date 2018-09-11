'use strict';

function mainHasBeenScrolled() {
  document.querySelector('header').classList.add('shadow');
  document.querySelector('.totop').classList.add('active');
}

function totop() {
  console.log(123)
  document.querySelector('main').scrollTo(0, 0);
}

