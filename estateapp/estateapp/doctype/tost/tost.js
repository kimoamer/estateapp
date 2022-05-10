// Copyright (c) 2022, test and contributors
// For license information, please see license.txt

frappe.ui.form.on('tost', {
	refresh: function(frm) {
    let slideIndex = 2;
    frm.showSlides = function (frm, n){
      let i;
      let slides = document.getElementsByClassName("mySlidess");
      let dots = document.getElementsByClassName("dot");
      if (n > slides.length) {slideIndex = 1}
      if (n < 1) {slideIndex = slides.length}
      for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
      }
      for (i = 0; i < dots.length; i++) {
        dots[i].className = dots[i].className.replace(" active", "");
      }
      slides[slideIndex-1].style.display = "block";
      dots[slideIndex-1].className += " active";
    }
    frm.showSlides(frm, slideIndex);

    frm.plusSlides = function (frm, n) {
      frm.showSlides(frm, slideIndex += n);
    }

    frm.currentSlide = function (frm, n) {
      frm.showSlides(frm, slideIndex = n);
    }
	},
  onload_post_render: function (frm) {
    var element = document.getElementById("dot1");
    element.onclick = function(event) {
      frm.currentSlide(frm,1);
    }
    var element2 = document.getElementById("dot2");
    element2.onclick = function(event) {
      frm.currentSlide(frm,2);
    }
    var element3 = document.getElementById("dot3");
    element3.onclick = function(event) {
      frm.currentSlide(frm,3);
    }
  }
});
