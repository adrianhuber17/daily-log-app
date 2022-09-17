import { useEffect, useState } from "react";

export default function Messages() {
  const [messages, setMessages] = useState([]);
  const [load, setLoad] = useState(false);

  useEffect(() => {
    fetch("/messages")
      .then((response) => response.json())
      .then((responseData) => {
        setMessages(responseData);
        setLoad(true);
        console.log(responseData);
      });
  }, []);

  if (messages.length === 0) {
    return <>{load && <p>No Messages</p>}</>;
  }

  return (
    <>
      {load &&
        messages.map((message) => (
          <li id={message.id} key={message.id}>
            Message: {message.text}, Date: {message.date}
          </li>
        ))}
    </>
  );
}
