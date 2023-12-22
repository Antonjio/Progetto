/*this file is used to set the background color of the keys selected in fumetto section with the color whitesmoke*/
document.addEventListener("DOMContentLoaded", () => {
  const latestButton = document.getElementById("latest");
  const ascButton = document.getElementById("asc");
  const descButton = document.getElementById("desc");

  if (latestButton && window.location.pathname === "/fumetto") {
    latestButton.style.cssText = "background-color: #71717A; color: whitesmoke";
  }

  if (ascButton && window.location.pathname === "/fumetto/price/asc") {
    handleStylePriceDropdownLinks(ascButton);
  }

  if (descButton && window.location.pathname === "/fumetto/price/desc") {
    handleStylePriceDropdownLinks(descButton);
  }

  ascButton.addEventListener("click", handleStylePriceAnchor);
  descButton.addEventListener("click", handleStylePriceAnchor);

  const mangaButton = document.getElementById("manga");
  const comicsButton = document.getElementById("comics");

  mangaButton.addEventListener("click", handleTypeBgInherit);
  comicsButton.addEventListener("click", handleTypeBgInherit);


  if (mangaButton && window.location.pathname === "/fumetto/type/manga") {
    handleStyleTypeDropdownLinks(mangaButton);
  }

  if (comicsButton && window.location.pathname === "/fumetto/type/comics") {
    handleStyleTypeDropdownLinks(comicsButton);
  }

});

function handleStylePriceAnchor() {
  const priceAnchor = document.getElementById("price");

  priceAnchor.style.cssText = "background-color: transparent !important";
}

function handleTypeBgInherit() {
  const categoryAnchor = document.getElementById("type");

  categoryAnchor.style.cssText = "background-color: transparent !important";
}

function handleStylePriceDropdownLinks(linkToStyle) {
  linkToStyle.style.cssText = "background-color: #71717A; color: whitesmoke";
  document.getElementById("price-dropdown").style.cssText =
    "transition: none !important; max-height: 200px !important";
}

function handleStyleTypeDropdownLinks(linkToStyle) {
  linkToStyle.style.cssText = "background-color: #71717A; color: whitesmoke";
  document.getElementById("type-dropdown").style.cssText =
    "transition: none !important; max-height: 200px !important";
}
