/*this file is used to set the background color of the keys selected in funko-pop section with the color whitesmoke*/
document.addEventListener("DOMContentLoaded", () => {
  const latestButton = document.getElementById("latest");
  const ascButton = document.getElementById("asc");
  const descButton = document.getElementById("desc");

  if (latestButton && window.location.pathname === "/funko") {
    latestButton.style.cssText = "background-color: #71717A; color: whitesmoke";
  }

  if (ascButton && window.location.pathname === "/funko/price/asc") {
    handleStylePriceDropdownLinks(ascButton);
  }

  if (descButton && window.location.pathname === "/funko/price/desc") {
    handleStylePriceDropdownLinks(descButton);
  }

  ascButton.addEventListener("click", handleStylePriceAnchor);
  descButton.addEventListener("click", handleStylePriceAnchor);

  const serieTvButton = document.getElementById("serietv");
  const filmButton = document.getElementById("film");
  const gameButton = document.getElementById("game");

  serieTvButton.addEventListener("click", handleCategoryBgInherit);
  filmButton.addEventListener("click", handleCategoryBgInherit);
  gameButton.addEventListener("click", handleCategoryBgInherit);

  if (serieTvButton && window.location.pathname === "/funko/category/serietv") {
    handleStyleCategoryDropdownLinks(serieTvButton);
  }

  if (
    filmButton &&
    window.location.pathname === "/funko/category/film"
  ) {
    handleStyleCategoryDropdownLinks(filmButton);
  }

  if (gameButton && window.location.pathname === "/funko/category/game") {
    handleStyleCategoryDropdownLinks(gameButton);
  }
});

function handleStylePriceAnchor() {
  const priceAnchor = document.getElementById("price");

  priceAnchor.style.cssText = "background-color: transparent !important";
}

function handleCategoryBgInherit() {
  const categoryAnchor = document.getElementById("category");

  categoryAnchor.style.cssText = "background-color: transparent !important";
}

function handleStylePriceDropdownLinks(linkToStyle) {
  linkToStyle.style.cssText = "background-color: #71717A; color: whitesmoke";
  document.getElementById("price-dropdown").style.cssText =
    "transition: none !important; max-height: 200px !important";
}

function handleStyleCategoryDropdownLinks(linkToStyle) {
  linkToStyle.style.cssText = "background-color: #71717A; color: whitesmoke";
  document.getElementById("category-dropdown").style.cssText =
    "transition: none !important; max-height: 200px !important";
}
