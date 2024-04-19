function convertCurrency() {
    var amount = document.getElementById("amount").value;
    var fromCurrency = document.getElementById("from_currency").value;
    var toCurrency = document.getElementById("to_currency").value;

    $.ajax({
        url: "http://currency.eba-qchvcgzv.us-east-1.elasticbeanstalk.com/convert",
        type: "GET",
        data: { amount: amount, from_currency: fromCurrency, to_currency: toCurrency },
        success: function(response) {
            document.getElementById("result").innerHTML = amount + " " + fromCurrency + " = " + response.converted_amount.toFixed(2) + " " + toCurrency;
        },
        error: function(_xhr, _status, error) {
            console.error(error);
            document.getElementById("result").innerHTML = "An error occurred. Please try again later.";
        }
    });
}

var current = null;
document.querySelector("#email").addEventListener("focus", function (e) {
  if (current) current.pause();
  current = anime({
    targets: "path",
    strokeDashoffset: {
      value: 0,
      duration: 700,
      easing: "easeOutQuart"
    },
    strokeDasharray: {
      value: "240 1386",
      duration: 700,
      easing: "easeOutQuart"
    }
  });
});
document.querySelector("#password").addEventListener("focus", function (e) {
  if (current) current.pause();
  current = anime({
    targets: "path",
    strokeDashoffset: {
      value: -336,
      duration: 700,
      easing: "easeOutQuart"
    },
    strokeDasharray: {
      value: "240 1386",
      duration: 700,
      easing: "easeOutQuart"
    }
  });
});
document.querySelector("#submit").addEventListener("focus", function (e) {
  if (current) current.pause();
  current = anime({
    targets: "path",
    strokeDashoffset: {
      value: -730,
      duration: 700,
      easing: "easeOutQuart"
    },
    strokeDasharray: {
      value: "530 1386",
      duration: 700,
      easing: "easeOutQuart"
    }
  });
});
