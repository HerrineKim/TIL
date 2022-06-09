import React, { useState } from "react";

function SignUp(props) {
  const [name, setName] = useState("");

  const handleChangeName = (event) => {
    setName(event.target.value);
  };

  const handleSubmit = (event) => {
    alert(`이름: ${name}`);
    event.preventDefault();
  };
}