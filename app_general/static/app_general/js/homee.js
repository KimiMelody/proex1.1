//----    debug    ----//
window.addEventListener('click', () => {
    console.log(1);
});
console.log('debug จ่ะ อิอิ');


//----    left-div event    ----//

//----    solution           ----//
document.addEventListener("DOMContentLoaded", function () {
  const showSolutionLinks = document.querySelectorAll(".showSolution");
  const imageContainers = document.querySelectorAll(".imageContainer");

  showSolutionLinks.forEach((link, index) => {
    link.addEventListener("click", function (event) {
      event.preventDefault();
      imageContainers[index].style.display = "block";
    });
  });

  const closeIcons = document.querySelectorAll(".close-icon");

  closeIcons.forEach((icon) => {
    icon.addEventListener("click", function () {
      const parentContainer = icon.closest(".imageContainer");
      parentContainer.style.display = "none";
    });
  });
});