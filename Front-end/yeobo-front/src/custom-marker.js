export default (google) => {
  return class CustomMarker extends google.maps.OverlayView {
    constructor(position, content, options = { classname: "custom-marker" }) {
      super();
      const { classname } = options;
      this.options = options;
      this.position = position;
      content.classList.add(classname);
      const bubbleAnchor = document.createElement("div");
      bubbleAnchor.classList.add(`${classname}-anchor`);
      bubbleAnchor.appendChild(content);
      this.containerDiv = document.createElement("div");
      this.containerDiv.classList.add(`${classname}-container`);
      this.containerDiv.appendChild(bubbleAnchor);
    }
    onAdd() {
      this.getPanes().floatPane.appendChild(this.containerDiv);
    }
    onRemove() {
      if (this.containerDiv.parentElement) {
        this.containerDiv.parentElement.removeChild(this.containerDiv);
      }
    }
    draw() {
      const divPosition = this.getProjection().fromLatLngToDivPixel(
        this.position
      );
      // Hide the popup when it is far out of view.
      const display =
        Math.abs(divPosition.x) < 4000 && Math.abs(divPosition.y) < 4000
          ? "block"
          : "none";

      if (display === "block") {
        this.containerDiv.style.left = divPosition.x + "px";
        this.containerDiv.style.top = divPosition.y + "px";
      }

      if (this.containerDiv.style.display !== display) {
        this.containerDiv.style.display = display;
      }
    }
  };
};