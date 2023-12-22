/*this file is used to set the background color of the keys selected in videogames section with the color whitesmoke*/
document.addEventListener("DOMContentLoaded", () => {
    const latestButton = document.getElementById("latest");
    const ascButton = document.getElementById("asc");
    const descButton = document.getElementById("desc");

    if (latestButton && window.location.pathname === "/videogames") {
        latestButton.style.cssText = "background-color: #71717A; color: whitesmoke";
    }

    if (ascButton && window.location.pathname === "/videogames/price/asc") {
        handleStylePriceDropdownLinks(ascButton);
    }

    if (descButton && window.location.pathname === "/videogames/price/desc") {
        handleStylePriceDropdownLinks(descButton);
    }

    ascButton.addEventListener("click", handleStylePriceAnchor);
    descButton.addEventListener("click", handleStylePriceAnchor);

    const actionButton = document.getElementById("action");
    const adventureButton = document.getElementById("adventure");
    const sportButton = document.getElementById("sport");

    actionButton.addEventListener("click", handleGenreBgInherit);
    adventureButton.addEventListener("click", handleGenreBgInherit);
    sportButton.addEventListener("click", handleGenreBgInherit);

    if (actionButton && window.location.pathname === "/videogames/genre/action") {
        handleStyleGenreDropdownLinks(actionButton);
    }

    if (
        adventureButton &&
        window.location.pathname === "/videogames/genre/adventure"
    ) {
        handleStyleGenreDropdownLinks(adventureButton);
    }

    if (sportButton && window.location.pathname === "/videogames/genre/sport") {
        handleStyleGenreDropdownLinks(sportButton);
    }
});

function handleStylePriceAnchor() {
    const priceAnchor = document.getElementById("price");

    priceAnchor.style.cssText = "background-color: transparent !important";
}

function handleGenreBgInherit() {
    const genreAnchor = document.getElementById("genre");

    genreAnchor.style.cssText = "background-color: transparent !important";
}

function handleStylePriceDropdownLinks(linkToStyle) {
    linkToStyle.style.cssText = "background-color: #71717A; color: whitesmoke";
    document.getElementById("price-dropdown").style.cssText =
        "transition: none !important; max-height: 200px !important";
}

function handleStyleGenreDropdownLinks(linkToStyle) {
    linkToStyle.style.cssText = "background-color: #71717A; color: whitesmoke";
    document.getElementById("genre-dropdown").style.cssText =
        "transition: none !important; max-height: 200px !important";
}
