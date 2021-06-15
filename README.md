# DjangoEcommerce

This is a Ecommerce web application made with Django framework. It provide editing system for main admin of the application and for customer to get the products to buy the products.

<hr>
<h3>The Sample Images outputs are:</h3>
<style>
* {box-sizing: border-box}
body {font-family: Verdana, sans-serif; margin:0}
.mySlides {display: none}
img {vertical-align: middle;}
/* Slideshow container */
.slideshow-container {
  max-width: 1000px;
  position: relative;
  margin: auto;
}
/* Next & previous buttons */
.prev, .next {
  cursor: pointer;
  position: absolute;
  top: 50%;
  width: auto;
  padding: 16px;
  margin-top: -22px;
  color: white;
  font-weight: bold;
  font-size: 18px;
  transition: 0.6s ease;
  border-radius: 0 3px 3px 0;
  user-select: none;
}
/* Position the "next button" to the right */
.next {
  right: 0;
  border-radius: 3px 0 0 3px;
}
/* On hover, add a black background color with a little bit see-through */
.prev:hover, .next:hover {
  background-color: rgba(0,0,0,0.8);
}
/* Caption text */
.text {
  color: #f2f2f2;
  font-size: 15px;
  padding: 8px 12px;
  position: absolute;
  bottom: 8px;
  width: 100%;
  text-align: center;
}
/* Number text (1/3 etc) */
.numbertext {
  color: #f2f2f2;
  font-size: 12px;
  padding: 8px 12px;
  position: absolute;
  top: 0;
}
/* The dots/bullets/indicators */
.dot {
  cursor: pointer;
  height: 15px;
  width: 15px;
  margin: 0 2px;
  background-color: #bbb;
  border-radius: 50%;
  display: inline-block;
  transition: background-color 0.6s ease;
}
.active, .dot:hover {
  background-color: #717171;
}
/* Fading animation */
.fade {
  -webkit-animation-name: fade;
  -webkit-animation-duration: 1.5s;
  animation-name: fade;
  animation-duration: 1.5s;
}
@-webkit-keyframes fade {
  from {opacity: .4} 
  to {opacity: 1}
}
@keyframes fade {
  from {opacity: .4} 
  to {opacity: 1}
}
/* On smaller screens, decrease text size */
@media only screen and (max-width: 300px) {
  .prev, .next,.text {font-size: 11px}
}
</style>
</head>
<body>

<div class="slideshow-container">

<div class="mySlides fade">
  <img src="img_nature_wide.jpg" style="width:100%">
  <div class="text">Caption Text</div>
</div>
<div class="mySlides fade">
  <img src="img_nature_wide.jpg" style="width:100%">
  <div class="text">Caption Text</div>
</div>
<div class="mySlides fade">
  <img src="img_nature_wide.jpg" style="width:100%">
  <div class="text">Caption Text</div>
</div>
<div class="mySlides fade">
  <img src="img_nature_wide.jpg" style="width:100%">
  <div class="text">Caption Text</div>
</div>
<div class="mySlides fade">
  <img src="img_nature_wide.jpg" style="width:100%">
  <div class="text">Caption Text</div>
</div>
<div class="mySlides fade">
  <img src="img_nature_wide.jpg" style="width:100%">
  <div class="text">Caption Text</div>
</div>

<div class="mySlides fade">
  <img src="img_nature_wide.jpg" style="width:100%">
  <div class="text">Caption Text</div>
</div>
<div class="mySlides fade">
  <img src="img_nature_wide.jpg" style="width:100%">
  <div class="text">Caption Text</div>
</div>
<div class="mySlides fade">
  <img src="img_nature_wide.jpg" style="width:100%">
  <div class="text">Caption Text</div>
</div>
<div class="mySlides fade">
  <img src="img_nature_wide.jpg" style="width:100%">
  <div class="text">Caption Text</div>
</div>
<div class="mySlides fade">
  <img src="img_nature_wide.jpg" style="width:100%">
  <div class="text">Caption Text</div>
</div>
<div class="mySlides fade">
  <img src="img_nature_wide.jpg" style="width:100%">
  <div class="text">Caption Text</div>
</div>

<div class="mySlides fade">
  <img src="img_nature_wide.jpg" style="width:100%">
  <div class="text">Caption Text</div>
</div>
<div class="mySlides fade">
  <img src="img_nature_wide.jpg" style="width:100%">
  <div class="text">Caption Text</div>
</div>
<div class="mySlides fade">
  <img src="img_nature_wide.jpg" style="width:100%">
  <div class="text">Caption Text</div>
</div>
<div class="mySlides fade">
  <img src="img_nature_wide.jpg" style="width:100%">
  <div class="text">Caption Text</div>
</div>
<div class="mySlides fade">
  <img src="img_nature_wide.jpg" style="width:100%">
  <div class="text">Caption Text</div>
</div>
<div class="mySlides fade">
  <img src="img_nature_wide.jpg" style="width:100%">
  <div class="text">Caption Text</div>
</div>
 
<div class="mySlides fade">
  <img src="img_nature_wide.jpg" style="width:100%">
  <div class="text">Caption Text</div>
</div>
<div class="mySlides fade">
  <img src="img_nature_wide.jpg" style="width:100%">
  <div class="text">Caption Text</div>
</div>
<div class="mySlides fade">
  <img src="img_nature_wide.jpg" style="width:100%">
  <div class="text">Caption Text</div>
</div>
<div class="mySlides fade">
  <img src="img_nature_wide.jpg" style="width:100%">
  <div class="text">Caption Text</div>
</div>
<div class="mySlides fade">
  <img src="img_nature_wide.jpg" style="width:100%">
  <div class="text">Caption Text</div>
</div>
<div class="mySlides fade">
  <img src="img_nature_wide.jpg" style="width:100%">
  <div class="text">Caption Text</div>
</div>
  
<div class="mySlides fade">
  <img src="img_nature_wide.jpg" style="width:100%">
  <div class="text">Caption Text</div>
</div>
<div class="mySlides fade">
  <img src="img_nature_wide.jpg" style="width:100%">
  <div class="text">Caption Text</div>
</div>
<div class="mySlides fade">
  <img src="img_nature_wide.jpg" style="width:100%">
  <div class="text">Caption Text</div>
</div>
<div class="mySlides fade">
  <img src="img_nature_wide.jpg" style="width:100%">
  <div class="text">Caption Text</div>
</div>
<div class="mySlides fade">
  <img src="img_nature_wide.jpg" style="width:100%">
  <div class="text">Caption Text</div>
</div>
<div class="mySlides fade">
  <img src="img_nature_wide.jpg" style="width:100%">
  <div class="text">Caption Text</div>
</div>
 
<div class="mySlides fade">
  <img src="img_nature_wide.jpg" style="width:100%">
  <div class="text">Caption Text</div>
</div>
<div class="mySlides fade">
  <img src="img_nature_wide.jpg" style="width:100%">
  <div class="text">Caption Text</div>
</div>
<div class="mySlides fade">
  <img src="img_nature_wide.jpg" style="width:100%">
  <div class="text">Caption Text</div>
</div>
<div class="mySlides fade">
  <img src="img_nature_wide.jpg" style="width:100%">
  <div class="text">Caption Text</div>
</div>

<a class="prev" onclick="plusSlides(-1)">&#10094;</a>
<a class="next" onclick="plusSlides(1)">&#10095;</a>

</div>
<br>

<div style="text-align:center">
  <span class="dot" onclick="currentSlide(1)"></span> 
  <span class="dot" onclick="currentSlide(2)"></span> 
  <span class="dot" onclick="currentSlide(3)"></span> 
  <span class="dot" onclick="currentSlide(4)"></span> 
  <span class="dot" onclick="currentSlide(5)"></span> 
  <span class="dot" onclick="currentSlide(6)"></span> 
  <span class="dot" onclick="currentSlide(7)"></span> 
  <span class="dot" onclick="currentSlide(8)"></span> 
  <span class="dot" onclick="currentSlide(9)"></span> 
  <span class="dot" onclick="currentSlide(10)"></span> 
  <span class="dot" onclick="currentSlide(11)"></span> 
  <span class="dot" onclick="currentSlide(12)"></span> 
  <span class="dot" onclick="currentSlide(13)"></span> 
  <span class="dot" onclick="currentSlide(14)"></span> 
  <span class="dot" onclick="currentSlide(15)"></span> 
  <span class="dot" onclick="currentSlide(16)"></span> 
  <span class="dot" onclick="currentSlide(17)"></span> 
  <span class="dot" onclick="currentSlide(18)"></span> 
  <span class="dot" onclick="currentSlide(19)"></span> 
  <span class="dot" onclick="currentSlide(20)"></span> 
  <span class="dot" onclick="currentSlide(21)"></span> 
  <span class="dot" onclick="currentSlide(22)"></span> 
  <span class="dot" onclick="currentSlide(23)"></span> 
  <span class="dot" onclick="currentSlide(24)"></span> 
  <span class="dot" onclick="currentSlide(25)"></span> 
  <span class="dot" onclick="currentSlide(26)"></span> 
  <span class="dot" onclick="currentSlide(27)"></span> 
  <span class="dot" onclick="currentSlide(28)"></span> 
  <span class="dot" onclick="currentSlide(29)"></span> 
  <span class="dot" onclick="currentSlide(30)"></span> 
  <span class="dot" onclick="currentSlide(31)"></span> 
  <span class="dot" onclick="currentSlide(32)"></span> 
  <span class="dot" onclick="currentSlide(33)"></span> 
  <span class="dot" onclick="currentSlide(34)"></span> 
</div>

<script>
var slideIndex = 1;
showSlides(slideIndex);

function plusSlides(n) {
  showSlides(slideIndex += n);
}

function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  var i;
  var slides = document.getElementsByClassName("mySlides");
  var dots = document.getElementsByClassName("dot");
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
</script>
<hr>

![Screenshot_15062021_182940](https://user-images.githubusercontent.com/58340159/122059709-8d447200-ce0a-11eb-8190-9190bb6a5b89.png)
![Screenshot_15062021_183039](https://user-images.githubusercontent.com/58340159/122059714-8ddd0880-ce0a-11eb-8920-570513400d28.png)
![Screenshot_15062021_183052](https://user-images.githubusercontent.com/58340159/122059721-8fa6cc00-ce0a-11eb-9bda-aa67b122d02b.png)
![Screenshot_15062021_183056](https://user-images.githubusercontent.com/58340159/122059727-91708f80-ce0a-11eb-9d4e-ba0e853547f0.png)
![Screenshot_15062021_183103](https://user-images.githubusercontent.com/58340159/122059730-92092600-ce0a-11eb-9860-15a79e46d213.png)
![Screenshot_15062021_183111](https://user-images.githubusercontent.com/58340159/122059736-93d2e980-ce0a-11eb-8f10-cb67dd993089.png)
![Screenshot_15062021_183116](https://user-images.githubusercontent.com/58340159/122059745-959cad00-ce0a-11eb-818f-429105a84581.png)
![Screenshot_15062021_183121](https://user-images.githubusercontent.com/58340159/122059748-959cad00-ce0a-11eb-97f3-ab7ff660bb17.png)
![Screenshot_15062021_183126](https://user-images.githubusercontent.com/58340159/122059752-96cdda00-ce0a-11eb-86ca-2f1c5e50e050.png)
![Screenshot_15062021_183131](https://user-images.githubusercontent.com/58340159/122059756-97ff0700-ce0a-11eb-9353-f636689dd17e.png)
![Screenshot_15062021_183137](https://user-images.githubusercontent.com/58340159/122059762-99303400-ce0a-11eb-822f-1053cc1d665c.png)
![Screenshot_15062021_183141](https://user-images.githubusercontent.com/58340159/122059767-9a616100-ce0a-11eb-9bb0-ec6c2620cb46.png)
![Screenshot_15062021_183634](https://user-images.githubusercontent.com/58340159/122059774-9af9f780-ce0a-11eb-8aa9-3e1c8a4d73b2.png)
![Screenshot_15062021_183645](https://user-images.githubusercontent.com/58340159/122059779-9b928e00-ce0a-11eb-882c-cced70df385f.png)
![Screenshot_15062021_183657](https://user-images.githubusercontent.com/58340159/122059784-9cc3bb00-ce0a-11eb-9540-f2edda4c0d01.png)
![Screenshot_15062021_183700](https://user-images.githubusercontent.com/58340159/122059792-9d5c5180-ce0a-11eb-8792-fc04f3cf7234.png)
![Screenshot_15062021_183706](https://user-images.githubusercontent.com/58340159/122059795-9e8d7e80-ce0a-11eb-8df8-b025c2d5edc0.png)
![Screenshot_15062021_183709](https://user-images.githubusercontent.com/58340159/122059799-9f261500-ce0a-11eb-8134-e0d143c2a677.png)
![Screenshot_15062021_183714](https://user-images.githubusercontent.com/58340159/122059803-9f261500-ce0a-11eb-9e50-baad5ad39ba5.png)
![Screenshot_15062021_183716](https://user-images.githubusercontent.com/58340159/122059806-9fbeab80-ce0a-11eb-8b75-04dc23ef8d59.png)
![Screenshot_15062021_183721](https://user-images.githubusercontent.com/58340159/122059807-a0574200-ce0a-11eb-8965-cfd708127837.png)
![Screenshot_15062021_183739](https://user-images.githubusercontent.com/58340159/122059810-a0efd880-ce0a-11eb-9e9c-6370e3f45541.png)
![Screenshot_15062021_183741](https://user-images.githubusercontent.com/58340159/122059812-a1886f00-ce0a-11eb-869f-7e0034e9fb3f.png)
![Screenshot_15062021_183757](https://user-images.githubusercontent.com/58340159/122059816-a2210580-ce0a-11eb-9bb7-81841a58669f.png)
![Screenshot_15062021_183820](https://user-images.githubusercontent.com/58340159/122059823-a3eac900-ce0a-11eb-8e01-1c99d3ae0b41.png)
![Screenshot_15062021_183841](https://user-images.githubusercontent.com/58340159/122059830-a4835f80-ce0a-11eb-9073-72fcc145d9ad.png)
![Screenshot_15062021_183855](https://user-images.githubusercontent.com/58340159/122059833-a5b48c80-ce0a-11eb-9ceb-4b852c540e09.png)
![Screenshot_15062021_183905](https://user-images.githubusercontent.com/58340159/122059836-a6e5b980-ce0a-11eb-9728-5dc0d491643f.png)
![Screenshot_15062021_184015](https://user-images.githubusercontent.com/58340159/122059839-a6e5b980-ce0a-11eb-9b9b-8870be7e20d6.png)
![Screenshot_15062021_184023](https://user-images.githubusercontent.com/58340159/122059841-a77e5000-ce0a-11eb-9916-e81a0692b9a1.png)
![Screenshot_15062021_184032](https://user-images.githubusercontent.com/58340159/122059844-a816e680-ce0a-11eb-9fb6-80d8938b8b1d.png)
![Screenshot_15062021_184045](https://user-images.githubusercontent.com/58340159/122059846-a8af7d00-ce0a-11eb-990c-44e3c39cbeec.png)
![Screenshot_15062021_184047](https://user-images.githubusercontent.com/58340159/122059849-a9481380-ce0a-11eb-9c80-9ab614b4a2aa.png)
![Screenshot_15062021_184049](https://user-images.githubusercontent.com/58340159/122059850-a9e0aa00-ce0a-11eb-9296-fd79d8274ccf.png)
