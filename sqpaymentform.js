// Set the application ID
var applicationId = "sandbox-sq0idp-jtBNwhdrdADhVZ6OLkRrMw";

// Set the location ID
var locationId = "CBASEGLb1fOhVH4Uvvi1aY_bOawgAQ";

/*
 * function: requestCardNonce
 *
 * requestCardNonce is triggered when the "Pay with credit card" button is
 * clicked
 *
 * Modifying this function is not required, but can be customized if you
 * wish to take additional action when the form button is clicked.
 */
function requestCardNonce(event) {

  // Don't submit the form until SqPaymentForm returns with a nonce
  event.preventDefault();

  // Request a nonce from the SqPaymentForm object
  paymentForm.requestCardNonce();
}

function showDiv() {
  // var checkBox = document.getElementById("box");
  // var customerInfo = document.getElementById("customer-info");

    // If the checkbox is checked, display the output text
  if (checkBox.checked == true){
    // customerInfo.style.display = "block";
    // checkBox.value = true;
    document.getElementById("box").value = "true";
  } else {
    // customerInfo.style.display = "none";
    // checkBox.value = false;
    document.getElementById("box").value = "false";
  }

}

// Create and initialize a payment form object
var paymentForm = new SqPaymentForm({

  // Initialize the payment form elements
  applicationId: 'sandbox-sq0idp-jtBNwhdrdADhVZ6OLkRrMw',
  locationId: 'CBASEGLb1fOhVH4Uvvi1aY_bOawgAQ',
  inputClass: 'sq-input',

  // Customize the CSS for SqPaymentForm iframe elements
  inputStyles: [{
      fontSize: '.9em'
  }],

  // Initialize Apple Pay placeholder ID
  applePay: {
    elementId: 'sq-apple-pay'
  },

  // // Initialize Masterpass placeholder ID
  // masterpass: {
  //   elementId: 'sq-masterpass'
  // },

  // Initialize the credit card placeholders
  cardNumber: {
    elementId: 'sq-card-number',
    placeholder: '•••• •••• •••• ••••'
  },
  cvv: {
    elementId: 'sq-cvv',
    placeholder: 'CVV'
  },
  expirationDate: {
    elementId: 'sq-expiration-date',
    placeholder: 'MM/YY'
  },
  postalCode: {
    elementId: 'sq-postal-code'
  },

  // SqPaymentForm callback functions
  callbacks: {

    /*
     * callback function: methodsSupported
     * Triggered when: the page is loaded.
     */
    methodsSupported: function (methods) {

      // var applePayBtn = document.getElementById('sq-apple-pay');
      // var applePayLabel = document.getElementById('sq-apple-pay-label');


      // // Only show the button if Apple Pay for Web is enabled
      // // Otherwise, display the wallet not enabled message.
      // if (methods.applePay === true) {
      //   applePayBtn.style.display = 'inline-block';
      //   applePayLabel.style.display = 'none' ;
      // }

    },

    /*
     * callback function: createPaymentRequest
     * Triggered when: a digital wallet payment button is clicked.
     */
    createPaymentRequest: function () {
      // The payment request below is provided as
      // guidance. You should add code to create the object
      // programmatically.
      // return {
      //   requestShippingAddress: true,
      //   currencyCode: "USD",
      //   countryCode: "US",
      //   total: {
      //     label: "Hakuna",
      //     amount: "{{REPLACE_ME}}",
      //     pending: false,
      //   },
      //   lineItems: [
      //     {
      //       label: "Subtotal",
      //       amount: "{{REPLACE_ME}}",
      //       pending: false,
      //     },
      //     {
      //       label: "Shipping",
      //       amount: "{{REPLACE_ME}}",
      //       pending: true,
      //     },
      //     {
      //       label: "Tax",
      //       amount: "{{REPLACE_ME}}",
      //       pending: false,
      //     }
      //   ]
      // };
    },

    /*
     * callback function: cardNonceResponseReceived
     * Triggered when: SqPaymentForm completes a card nonce request
     */
    cardNonceResponseReceived: function(errors, nonce, cardData) {
      if (errors) {
        // Log errors from nonce generation to the Javascript console
        console.log("Encountered errors:");
        errors.forEach(function(error) {
          console.log('  ' + error.message);
        });

        return;
      }

      alert('Nonce received: ' + nonce); /* FOR TESTING ONLY */

      // Assign the nonce value to the hidden form field
      document.getElementById('card-nonce').value = nonce;

      var checkbox = document.getElementById("checkBox");
      if (checkbox.value == true) {
        var firstName = document.getElementById("firstname");
        var lastName = document.getElementById("lastname");
        var email = document.getElementById("email");
        // var box = document.getElementById("box");

        document.getElementById('firstname').value = firstName;
        document.getElementById('lastname').value = lastName;
        document.getElementById('email').value = email;
        // document.getElementById('box').value = "true";
      }

      // POST the nonce form to the payment processing page
      document.getElementById('nonce-form').submit();

    },

    /*
     * callback function: unsupportedBrowserDetected
     * Triggered when: the page loads and an unsupported browser is detected
     */
    unsupportedBrowserDetected: function() {
      /* PROVIDE FEEDBACK TO SITE VISITORS */
      alert('Brower not supported'); /* FOR TESTING ONLY */

    },

    /*
     * callback function: inputEventReceived
     * Triggered when: visitors interact with SqPaymentForm iframe elements.
     */
    inputEventReceived: function(inputEvent) {
      switch (inputEvent.eventType) {
        case 'focusClassAdded':
          /* HANDLE AS DESIRED */
          break;
        case 'focusClassRemoved':
          /* HANDLE AS DESIRED */
          break;
        case 'errorClassAdded':
          /* HANDLE AS DESIRED */
          break;
        case 'errorClassRemoved':
          /* HANDLE AS DESIRED */
          break;
        case 'cardBrandChanged':
          /* HANDLE AS DESIRED */
          break;
        case 'postalCodeChanged':
          /* HANDLE AS DESIRED */
          break;
      }
    },

    /*
     * callback function: paymentFormLoaded
     * Triggered when: SqPaymentForm is fully loaded
     */
    paymentFormLoaded: function() {
      /* HANDLE AS DESIRED */
    }
  }
});
