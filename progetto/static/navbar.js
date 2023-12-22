const root = "/";

/**
 * Function to load navbar
 */
export function loadNavbar() {
  fetch("/navbar")
    .then((response) => response.text())
    .then(async (html) => {
      document.getElementById("navbar").innerHTML = html;

      handleNavbarClass();

      window.addEventListener("resize", handleNavbarClass);

      toggleResponsiveNavbar();

      const loginButton = document.createElement("button");
      loginButton.id = "nav-login-button";
      loginButton.type = "button";
      loginButton.className = "cart-button";
      loginButton.style.textTransform = "uppercase";
      loginButton.innerHTML = "Login <i class='fas fa-user'></i>";

      loginButton.setAttribute("data-bs-toggle", "modal");
      loginButton.setAttribute("data-bs-target", "#loginModal");

      const loginButtonResponsive = document.createElement("button");
      loginButtonResponsive.id = "nav-login-button-responsive";
      loginButtonResponsive.type = "button";
      loginButtonResponsive.className = "cart-button";
      loginButtonResponsive.style.textTransform = "uppercase";
      loginButtonResponsive.innerHTML = "Login <i class='fas fa-user'></i>";

      loginButtonResponsive.setAttribute("data-bs-toggle", "modal");
      loginButtonResponsive.setAttribute("data-bs-target", "#loginModal");

      document.getElementById("actions").appendChild(loginButton);
      document
        .getElementById("actions-responsive")
        .appendChild(loginButtonResponsive);

      const userCard = document.getElementById("user-card");
      userCard.style.display = "none";

      const userButton = document.getElementById("user-button");
      userButton.style.display = "none";

      const userCardResponsive = document.getElementById(
        "user-card-responsive"
      );
      userCardResponsive.style.display = "none";

      const userButtonResponsive = document.getElementById(
        "user-button-responsive"
      );
      userButtonResponsive.style.display = "none";

      const cartBtn = document.getElementById("cart-btn");
      if (cartBtn) {
        cartBtn.addEventListener("click", handleCart);
      }

      const cartBtnResponsive = document.getElementById("cart-btn-responsive");
      if (cartBtnResponsive) {
        cartBtnResponsive.addEventListener("click", () => handleCart());
      }

      fetch("/user")
        .then((response) => {
          if (response.ok) {
            return response.json();
          } else {
            throw Error("Error getting user");
          }
        })
        .then(
          /**
           * @param {UserResponse} data The data response returned by server
           */
          (data) => {
            if (data.status !== 401) {
              const user = data.user;

              loginButton.remove();
              loginButtonResponsive.remove();

              userButton.style.cssText =
                "display: flex !important; border-radius: 100% !important;";

              userButtonResponsive.style.cssText =
                "display: flex !important; border-radius: 100% !important";

              userButton.addEventListener("click", () =>
                toggleUserCard(user, userButton, userCard)
              );

              userButtonResponsive.addEventListener("click", () => {
                toggleUserCard(user, userButtonResponsive, userCardResponsive);
              });

              const logoutButton = document.getElementById("logout-button");
              logoutButton.addEventListener("click", logout);

              const logoutButtonResponsive = document.getElementById(
                "logout-button-responsive"
              );
              logoutButtonResponsive.addEventListener("click", logout);
            }
          }
        );
    })
    .catch((error) => console.error("Error loading page content:", error));
}

/**
 * Function to toggle the user card when user button has clicked
 * @param {User} user The logged-in user
 * @param {HTMLButtonElement} userButton The user button to click to toggle the user card
 * @param {HTMLDivElement} userCard The user card to toggle
 */
function toggleUserCard(user, userButton, userCard) {
  userCard.style.display = userCard.style.display === "none" ? "block" : "none";

  userButton.classList.toggle(
    "user-button-open",
    userCard.style.display === "block"
  );

  userButton.setAttribute("aria-expanded", userCard.style.display === "block");

  const userFirstName = document.getElementById("user-firstName");
  const userLastName = document.getElementById("user-lastName");
  const userEmail = document.getElementById("user-email");

  userFirstName.innerHTML = user.firstName;
  userLastName.innerHTML = user.lastName;
  userEmail.innerHTML = user.email;

  const userFirstNameResponsive = document.getElementById(
    "user-firstName-responsive"
  );
  const userLastNameResponsive = document.getElementById(
    "user-lastName-responsive"
  );
  const userEmailResponsive = document.getElementById("user-email-responsive");

  userFirstNameResponsive.innerHTML = user.firstName;
  userLastNameResponsive.innerHTML = user.lastName;
  userEmailResponsive.innerHTML = user.email;
}

/**
 * @typedef {Object} LogoutResponse
 * @property {string} message The message returned by server
 * @property {string} status The response status
 */

/**
 * Function to do logout
 * If logout goes well, there'll be the redirect to homepage
 */
function logout() {
  fetch("/logout", {
    method: "POST",
  })
    .then((response) => {
      if (!response.ok) {
        throw Error("Error logging out");
      }

      return response.json();
    })
    .then(
      /**
       * Function called after response get
       * @param {LogoutResponse} data The data contained into response
       */
      (data) => {
        if (data.status === 200) {
          window.location.href = "/";
        }
      }
    );
}

/**
 * Function to manage responsive navbar
 */
function handleNavbarClass() {
  const navbar = document.getElementById("navbar");
  const responsiveNavbar = document.getElementById("responsive-navbar");

  if (responsiveNavbar.style.display === "flex") {
    navbar.style.cssText = "padding: 0 !important; margin: 0 !important";
  }
}

/**
 * Function to toggle responsive navbar
 */
function toggleResponsiveNavbar() {
  const menuButton = document.getElementById("menu-button");
  const menu = document.getElementById("dropdown-responsive");

  menuButton.addEventListener("click", (e) => {
    e.preventDefault();

    menu.classList.toggle("active");
    menuButton.classList.toggle("active");
  });
}

// Function to handle the cart action
function handleCart() {
  fetch("/store", {
    method: "POST",
  })
    .then(function (response) {
      if (!response.ok) {
        throw new Error("Request failed");
      }

      return response.json();
    })
    .then((data) => {
      if ("not_logged" in data) {
        alert(data.not_logged); //error if a not logged user tries to open the cart
      } else if ("success" in data) {
        window.location.href = data.redirect_url;
      }
    })
    .catch(function (error) {
      console.log(error);
      alert("Request failed: " + error.message);
    });
}