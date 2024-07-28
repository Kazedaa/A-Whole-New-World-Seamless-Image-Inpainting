const draggable = document.getElementById("patch");
const container = document.getElementById("image");
const rect = container.getBoundingClientRect();
const y=rect.top;
const x=rect.left;


dragElement(draggable);

function dragElement(element , container) {
var pos1 = 0, pos2 = 0, pos3 = 0, pos4 = 0;
element.onmousedown = dragMouseDown;

function dragMouseDown(e) {
    e = e || window.event;
    e.preventDefault();
    // get the mouse cursor position at startup:
    pos3 = e.clientX;
    pos4 = e.clientY;
    document.onmouseup = closeDragElement;
    // call a function whenever the cursor moves:
    document.onmousemove = elementDrag;
}

function elementDrag(e) {
    e = e || window.event;
    e.preventDefault();
    // calculate the new cursor position:
    pos1 = pos3 - e.clientX;
    pos2 = pos4 - e.clientY;
    pos3 = e.clientX;
    pos4 = e.clientY;

    new_top = element.offsetTop - pos2;
    new_left = element.offsetLeft - pos1;

    // set the element's new position:
    if (y <= new_top && y + 128 -64 >= new_top)element.style.top = new_top + "px";
    else if(y > new_top)element.style.top = y + "px";
    else if(y + 128 -64 < new_top) element.style.top = y + 128 -64 + "px";

    if (x <= new_left && x + 128 -64 >= new_left)element.style.left = new_left + "px";
    else if(x > new_left)element.style.left = x + "px";
    else if(x + 128 -64 < new_left) element.style.left = x + 128 -64 + "px";

}

function closeDragElement() {
    // stop moving when mouse button is released:
    document.onmouseup = null;
    document.onmousemove = null;
}
}