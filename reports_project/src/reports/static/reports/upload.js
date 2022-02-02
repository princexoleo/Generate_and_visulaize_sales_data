
const csrf = document.getElementsByName('csrfmiddlewaretoken')[0].value;
const alertBox = document.getElementById('alert-box');



//

const handleAlerts = (type, msg) => {
    alertBox.innerHTML = `
        <div class="alert alert-${type}" role="alert">
            ${msg}
        </div>
    `
}
//console.log("CSRF: " + csrf);
Dropzone.autoDiscover = false;
const myDropzone = new Dropzone('#my-dropzone', {
    url: '/reports/upload/',
    init: function() {
        this.on('sending', function(file, xhr, formData){
            console.log('sending')
            formData.append('csrfmiddlewaretoken', csrf)
        })
        this.on('success', function(file, response){
            console.log(response.msg)
            if(response.msg) {
                handleAlerts('danger', 'File already exists')
            } else {
                handleAlerts('success', 'Your file has been uploaded')
            }
        })
    },
    maxFiles: 3,
    maxFilesize: 3,
    acceptedFiles: '.csv'
})

    


// const myDropzone = new Dropzone("#my-dropzone", {
//     url: "/reports/upload/",
//     init: function() {
//         this.on('sending', function(file, xhr, formData) {
//             console.log('Sending ...')
//             formData.append('csrfmiddlewaretoken', csrf);
            
//         })
//     }
// });
