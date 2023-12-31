console.log("Sanity check!");

// new
// Get Stripe publishable key
fetch("/config/")
.then((result) => { return result.json(); })
.then((data) => {
  // Initialize Stripe.js
  const stripe = Stripe(data.publicKey);
});

document.querySelector("#submitBtn").addEventListener("click", () => {
  // Get Checkout Session ID
  fetch("/cart/")
    .then((result) => { return result.json(); })
    .then((data) => {
      console.log(data);

      // Redirect to Stripe Checkout
      return stripe.redirectToCheckout({
        sessionId: data.sessionId,
        lineItems: [{ price: data.priceId }], // Use price and quantity
      });
    })
    .then((res) => {
      console.log(res);
    });
});
