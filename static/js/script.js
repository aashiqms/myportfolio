
// Django built in js function for handling csrf request to api's

		function getCookie(name) {
		    let cookieValue = null;
		    if (document.cookie && document.cookie !== '') {
		        let cookies = document.cookie.split(';');
		        for (let i = 0; i < cookies.length; i++) {
		            let cookie = cookies[i].trim();
		            // Does this cookie string begin with the name we want?
		            if (cookie.substring(0, name.length + 1) === (name + '=')) {
		                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
		                break;
		            }
		        }
		    }
		    return cookieValue;
		}
		let csrftoken = getCookie('csrftoken');

// .....................................................................................................................

		let activeItem = null
		let list_snapshot = []

// .....................................................................................................................

// https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch

// Function to display all projects

buildList()

		function buildList(){

			let url = '/api/project-list/';

			fetch(url)
			.then((resp) => resp.json())
			.then(function(data){
				console.log('Data:', data)

				let list = data;
				list.forEach((element, i) => {
					let details = `<p>${list[i].title}</p>
                                  <p>${list[i].description}</p>  
                                 `
					let item = `	
						<li class="item" style="color: white;list-style: none;margin-right: 10px;margin-left: 10px">
          ${details}
      </li>
</div>
					`
                    let items = document.getElementById('items')
					wrapper.innerHTML += item
                    items.innerHTML += item
                    console.log(item)
				})



			})
		}