import '../scss/styles.js';
import { useState, React, useEffect } from "react";


const defaultTopic = [
    {'id': 0, 'source': 'banana', 'translation': 'platana'},
    {'id': 1, 'source': 'banana', 'translation': 'platana'},
    {'id': 2, 'source': 'banana', 'translation': 'platana'},
    {'id': 3, 'source': 'banana', 'translation': 'platana'},
    {'id': 4, 'source': 'banana', 'translation': 'platana'},
    {'id': 5, 'source': 'banana', 'translation': 'platana'},
    {'id': 6, 'source': 'banana', 'translation': 'platana'},
    {'id': 7, 'source': 'banana', 'translation': 'platana'}
]

function TopicView (props) {
  const [topic, setTopic] = useState([]);

  useEffect(() => {
    const data = [
      {'username': props.userName}
    ]

    setTopic(defaultTopic);
    return;
      
    async function getTopic(userName) {
      await fetch("/user/topics", {
        method: 'GET',
        headers: {
          "Content-Type": "application/json",
          "Accept": "application/json"
        },
        body: JSON.stringify(data)
      }).then((res) => res.json()).then( (res2) => {

      }
      );
    }

    getTopic();

  }, [props.userName]);

  return (
    <>
      <ul className='topic-view-container'>
        {
          topic.map((pair) => { 
            return (
              <li key={pair.id}>
                <div id='pair-source'>{pair.source}</div>
                <div id='pair-target'>{pair.translation}</div>
                <button id='pair-delete-btn' onClick={() => this.deletePair(pair.id)}></button>
              </li>
            );
            })
        }
      </ul>
    </>
  );
}

export default TopicView;