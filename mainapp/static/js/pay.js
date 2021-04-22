
  var form = document.getElementById('payment-form');
  var stripe = Stripe('Ваш апи ключ тестовый');
  var elements = stripe.elements();
  var style = {
    base: {
        color: "#32325d",
      }
  };
 
  var card = elements.create("card", { style: style });
  card.mount("#card-element");
  card.on('change', function(event) {
    var displayError = document.getElementById('card-errors');
    if (event.error) {
        displayError.textContent = event.error.message;
      } else {
        displayError.textContent = '';
      }
    });
  form.addEventListener('submit', function(ev) {
    ev.preventDefault();
    var clientSecret = document.getElementById('card-button')
    stripe.confirmCardPayment(clientSecret.dataset.secret, {
      payment_method: {
        card: card,
        billing_details: {
          name: document.getElementById('card-button').dataset.username
        }
      }
    }).then(function(result) {
      if (result.error) {
        // Show error to your customer (e.g., insufficient funds)
        console.log(result.error.message);
      } else {
        // The payment has been processed!
        if (result.paymentIntent.status === 'succeeded') {
            function getCookie(name) {
                let cookieValue = null;
                if (document.cookie && document.cookie !== '') {
                    const cookies = document.cookie.split(';');
                    for (let i = 0; i < cookies.length; i++) {
                        const cookie = cookies[i].trim();
                        // Does this cookie string begin with the name we want?
                        if (cookie.substring(0, name.length + 1) === (name + '=')) {
                            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                            break;
                        }
                    }
                }
                return cookieValue;
            }
            const csrftoken = getCookie('csrftoken');
            var formData = new FormData(document.forms.order);
 
            // добавить к пересылке ещё пару ключ - значение
            formData.append("first_name", document.getElementById('card-button').dataset.username);
            formData.append("csrfmiddlewaretoken", csrftoken)
            var xhr = new XMLHttpRequest();
            xhr.open("POST", "/payed-online-order/");
            xhr.send(formData);
            xhr.onreadystatechange = function() {
                if (xhr.readyState == 4) {
                  window.location.replace("http://127.0.0.1:8000");
                  alert('Ваш заказ успешно оплачен! Менеджер с Вами свяжется')
                }
            }
        }
      }
    });
  });
