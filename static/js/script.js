
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

				data.forEach((element, i) => {

					let details = `<p><span class="heading-green">Project Name: </span></p>
									<p>${element.title}</p>
									<p><span class="heading-green">Description: </span></p>
									<p>${element.description}</p>
									<p><span class="heading-green">Source Code: </span></p>
									<p>
									<a href="${element.project_url}" style="text-decoration: none;
									color: orange">${element.project_url}</a></p>
                                 `
					console.log('element', element)
					let item = `	
						<li class="item" style="color: white;list-style: none;margin-right: 10px;margin-left: 10px">
          ${details}
      </li>
</div>
					`
                    let items = document.getElementById('items')
                    items.innerHTML += item
                    console.log(item)
				})



			})
		}