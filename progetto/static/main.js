window.onload = () => {
  "use strict";

  if ("serviceWorker" in navigator) {
    navigator.serviceWorker.register("/sw").then(
      function (registration) {
        // Service worker registered correctly.
        console.log(
          "ServiceWorker registration successful with scope: ",
          registration.scope
        );
      },
      function (err) {
        // Troubles in registering the service worker. :(
        console.log("ServiceWorker registration failed: ", err);
      }
    );
  }
};
// Execute when the DOM content is fully loaded
document.addEventListener("DOMContentLoaded", () => {
  // Load the list of countries in a dropdown of registration modal
  loadSelectCountries();

  // Attach event listeners for login and registration buttons
  const loginButton = document.getElementById("login-button");
  if (loginButton) {
    loginButton.addEventListener("click", handleLogin);
  }

  const registrationButton = document.getElementById("registration-button");
  if (registrationButton) {
    registrationButton.addEventListener("click", handleRegistration);
  }
});

// Function to perform a search based on user input
function search() {
  const searchTerm = document.getElementById("searchInput").value;
  window.location.href = "/search?term=" + searchTerm;
}

// Function to handle user login
function handleLogin() {
  const loginForm = document.getElementById("login");
  const submitHandler = function (ev) {
    ev.preventDefault();

    const formData = new FormData(loginForm);

    fetch("/login", {
      method: "POST",
      body: formData,
    })
      .then(function (response) {
        if (!response.ok) {
          throw new Error("Login failed");
        }

        return response.json();
      })
      .then((data) => {
        if ("error" in data) {
          alert(data.error);
        }

        if ("warning" in data) {
          alert(data.warning);
        }

        if ("success" in data) {
          window.location.href = "/";
        }

        loginForm.removeEventListener("submit", submitHandler);
      })
      .catch(function (error) {
        alert("Login failed: ", error);
      });
  };
  loginForm.addEventListener("submit", submitHandler);
}

// Function to handle user registration
function handleRegistration() {
  const registrationForm = document.getElementById("registration");
  const submitHandler = function (ev) {
    ev.preventDefault();

    const formData = new FormData(registrationForm);
    console.log(formData);

    fetch("/registration", {
      method: "POST",
      body: formData,
    })
      .then(function (response) {
        if (!response.ok) {
          throw new Error("Login failed");
        }

        return response.json();
      })
      .then((data) => {
        if ("error" in data) {
          alert(data.error);
        }

        if ("warning" in data) {
          alert(data.warning);
        }

        if ("success" in data) {
          window.location.href = "/";
        }

        registrationForm.removeEventListener("submit", submitHandler);
      })
      .catch(function (error) {
        alert("Registration failed: ", error);
      });
  };
  registrationForm.addEventListener("submit", submitHandler);
}

// Function to scroll to the top of the page
function scrollToTop() {
  window.scrollTo({
    top: 0,
    behavior: "smooth", // Option for smoother scrolling (requires modern browser support)
  });
}

// Function to close the error modal
function closeErrorModal() {
  document.getElementById("errorModal").style.display = "none";
}

/**
 * Load the dropdown with all countries
 */
function loadSelectCountries() {
  const select = document.getElementById("country");

  if (select) {
    // Fetch and populate the dropdown with countries
    fetch("https://restcountries.com/v3.1/all")
      .then((response) => response.json())
      .then((countries) => {
        countries
          .sort((a, b) => a.name.common.localeCompare(b.name.common))
          .forEach((country) => {
            const option = document.createElement("option");
            option.value = country.name.common.toLowerCase();
            option.text = country.name.common;
            select.add(option);
          });
      })
      .catch((error) => console.error("Error fetching countries:", error));
  }
}

// Function to handle adding an item to the cart
function handleAddItemToCart(formId) {
  const form = document.getElementById(formId);

  const submitHandler = function (ev) {
    ev.preventDefault();

    const formData = new FormData(form);

    fetch("/store", {
      method: "POST",
      body: formData,
    })
      .then(function (response) {
        if (!response.ok) {
          throw new Error("Login failed");
        }

        return response.json();
      })
      .then((data) => {
        if ("not_logged" in data) {
          alert(data.not_logged);
        }

        if ("success" in data) {
          window.location.href = data.redirect_url;
        }

        if ("already_added" in data) {
          //error if an item is already added to the cart
          alert(data.already_added);
        }

        form.removeEventListener("submit", submitHandler);
      })
      .catch(function (error) {
        alert("Buy form failed: ", error);
      });
  };
  form.addEventListener("submit", submitHandler);
}
