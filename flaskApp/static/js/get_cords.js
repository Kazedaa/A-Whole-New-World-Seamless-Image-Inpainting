function send_data(){
    const draggable = document.getElementById("patch");
    const container = document.getElementById("image");
    const rect_out = container.getBoundingClientRect();
    const rect_in = draggable.getBoundingClientRect();

    const image = document.getElementById("sample").src;

    const x = rect_in.left - rect_out.left;
    const y = rect_in.top - rect_out.top;

    const coords=[{
        'x' : x,
        'y' : y,
        'file' : image
    }];
    try {
        fetch(`${window.origin}/result`,{
            method : "POST",
            credentials : "include",
            body : JSON.stringify(coords),
            cache : "no-cache",
            headers : new Headers({
                "content-type": "application/json",
              })
        }).then((response) => {
            return response.text();
        }).then((html) => {
            document.body.innerHTML = html
        });

    }catch(error) {
        console.log("Error" , error);
    }
}