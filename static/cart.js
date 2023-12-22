let selectedItems = [];

// Main function executed when the DOM is fully loaded
document.addEventListener("DOMContentLoaded", () => {
  // Get items in the cart on startup
  getItemsCart();

  // Wait for 1 second before loading selected items
  setTimeout(() => {
    loadSelectedItems();
  }, 1000);

  // Add a listener for the payment form submission
  const paymentForm = document.getElementById("payment");
  paymentForm.addEventListener("submit", function (event) {
    event.preventDefault();
    handleOrderPayment();
  });
});

// Handles click on the checkbox of an item in the cart
function handleCheck(itemEan, selectedItem) {
  // Get references to the checkbox elements
  const checkbox = document.getElementById(`checkbox-${itemEan}`);
  const icon = document.getElementById(`icon-checkbox-${itemEan}`);

  // Find the index of the selected item in the array
  const itemIndex = selectedItems.indexOf(selectedItem);

  // If the item is not already selected, add it to the list
  if (itemIndex === -1) {
    // Update the style and class of the checkbox
    icon.classList.remove("not-checked");
    icon.classList.add("checked");
    checkbox.style.cssText =
      "background-color: #3498db !important; padding: 2px !important;";

    // Add the item to the list of selected items
    selectedItems.push(selectedItem);
    console.log(selectedItems);

    // Calculate and update the total amount
    calculateTotal();
  } else {
    // If the item is already selected, remove it from the list
    icon.classList.remove("checked");
    icon.classList.add("not-checked");
    checkbox.style.cssText =
      "background-color: transparent !important; padding: 12px !important;";

    selectedItems.splice(itemIndex, 1);
    console.log(selectedItems);

    // Calculate and update the total amount
    calculateTotal();
  }
}

// Calculates and updates the total amount of selected products
function calculateTotal() {
  let total = 0;

  // Get items in the cart from the server
  fetch("/cart/items")
    .then((response) => response.json())
    .then((data) => {
      if (data.length === 0) {
        document.getElementById("amount-card").style.cssText =
          "display: none !important";
      }

      // Iterate over the items and sum the prices of the selected items
      data.forEach((item) => {
        const icon = document.getElementById(`icon-checkbox-${item.ean}`);

        if (icon.classList.contains("checked")) {
          total += item.prezzo;
        }
      });

      // Update the HTML element with the total amount
      document.getElementById(
        "totalAmount"
      ).innerText = `${total.toLocaleString("de-DE", {
        minimumFractionDigits: 2,
        maximumFractionDigits: 2,
        useGrouping: true,
      })} €`;
    });
}

// Gets the items in the cart from the server
function getItemsCart() {
  fetch("/cart/items")
    .then((response) => response.json())
    .then((data) => {
      if (data.length === 0) {
        document.getElementById("amount-card").style.cssText =
          "display: none !important";
      }

      // Sort the items by descending addition date
      data.sort(
        (a, b) => new Date(b.data_aggiunta) - new Date(a.data_aggiunta)
      );

      // Get a reference to the table body in the document
      const tableBody = document.getElementById("cart-table-body");

      // Iterate over the items and create table rows
      data.forEach((item) => {
        calculateTotal(item);

        selectedItems.push(item.ean);

        const row = document.createElement("tr");

        const rowDataCheckbox = document.createElement("td");
        rowDataCheckbox.classList.add("t-body");
        rowDataCheckbox.style.cssText =
          "text-align: center !important; min-width: 5rem !important";

        const checkbox = document.createElement("button");
        checkbox.classList.add("btn-checkbox", "btn");
        checkbox.id = `checkbox-${item.ean}`;
        checkbox.setAttribute("data-item-id", item.ean);

        checkbox.addEventListener("click", () =>
          handleCheck(item.ean, item.ean)
        );

        const icon = document.createElement("i");
        icon.classList.add(
          "bi",
          "bi-check",
          "align-items-center",
          "justify-content-center",
          "checked"
        );
        icon.style.cssText = "font-size: 20px !important;";
        icon.id = `icon-checkbox-${item.ean}`;

        checkbox.appendChild(icon);

        rowDataCheckbox.appendChild(checkbox);

        row.appendChild(rowDataCheckbox);

        const rowDataItemImg = document.createElement("td");
        rowDataItemImg.classList.add("t-body");

        const itemImg = document.createElement("img");
        itemImg.classList.add("product-img");

        itemImg.src = `../static/image/${item.image}`;
        itemImg.alt = item.name;

        rowDataItemImg.appendChild(itemImg);

        row.appendChild(rowDataItemImg);

        const rowDataItemName = document.createElement("td");
        rowDataItemName.classList.add("t-body", "w-100");
        rowDataItemName.innerText = item.name;

        row.appendChild(rowDataItemName);

        const rowDataItemPrice = document.createElement("td");
        rowDataItemPrice.classList.add("t-body", "w-100");
        rowDataItemPrice.innerText = `${item.prezzo.toLocaleString("de-DE", {
          minimumFractionDigits: 2,
          maximumFractionDigits: 2,
          useGrouping: true,
        })} €`;

        row.appendChild(rowDataItemPrice);

        const rowDataActions = document.createElement("td");
        rowDataActions.classList.add("t-body");

        const removeItemForm = document.createElement("form");
        removeItemForm.action = `/remove/${item.ean}`;
        removeItemForm.method = "POST";

        const removeItemButton = document.createElement("button");
        removeItemButton.classList.add("delete-button");

        const removeItemIcon = document.createElement("i");
        removeItemIcon.classList.add(
          "bi",
          "bi-trash",
          "align-items-center",
          "justify-content-center",
          "d-flex"
        );
        removeItemIcon.style.cssText = "font-size: 27px !important;";

        removeItemButton.appendChild(removeItemIcon);

        removeItemForm.appendChild(removeItemButton);

        rowDataActions.appendChild(removeItemForm);

        row.appendChild(rowDataActions);

        tableBody.appendChild(row);
      });
    });
}

// Loads items that have been previously selected
function loadSelectedItems() {
  fetch("/cart/items")
    .then((response) => response.json())
    .then((data) => {
      // Iterate over the items and add the selected ones to selectedItems
      data.forEach((item) => {
        const icon = document.getElementById(`icon-checkbox-${item.ean}`);

        if (icon.classList.contains("checked")) {
          if (!selectedItems.includes(item.ean)) {
            selectedItems.push(item.ean);
          }
        }
      });

      // Remove duplicates from selectedItems
      selectedItems = Array.from(new Set(selectedItems));
    });
}

// Handles the order payment processing
function handleOrderPayment() {
  // Check if there are selected items in the cart
  if (selectedItems.length === 0) {
    alert("Select at least one item in the cart before proceeding to order.");
    return;
  }

  // Get the total amount from the document
  const totalAmountElement = document.getElementById("totalAmount");
  const totalAmount = parseFloat(
    totalAmountElement.innerText.replace("€", "").replace(",", "")
  );

  // Execute the AJAX request to call the Flask route
  fetch("/create-checkout-session", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ amount: totalAmount }), // Pass the amount in cents
  })
    .then((response) => response.json())
    .then((data) => {
      // Empty the cart after a successful purchase
      emptyCart();

      // Redirect to the Stripe payment page
      window.location.replace(data.redirect);
    })
    .catch((error) => {
      console.error("Error creating payment session:", error);
    });
}

// Empties the cart by sending a request to the server
function emptyCart() {
  fetch("/empty-cart", {
    method: "POST",
  })
    .then((response) => response.json())
    .then((data) => {
      console.log("Cart emptied successfully");
      // You can do something else here if needed
    })
    .catch((error) => {
      console.error("Error emptying the cart:", error);
    });
}
