function passwordShow() {
    let pass = document.querySelector(".password");
    let passImg = document.querySelector(".passImg");
    if (pass.type === "password") {
      pass.type = "text";
      passImg.src = "../../media/icons/eye-hidden.svg";
    } else {
      pass.type = "password";
      passImg.src = "../../media/icons/eye.svg";
    }
  }