import React, { useEffect, useState } from 'react';
import '../styles/styles';

function TopicView () {
    const [list, setList] = useState([]);

    const [openTopic, setOpenTopic] = useState('Fruit');

    useEffect(() => {
        const getList = async () => {
            const requestOptions = {
              method: 'POST',
              headers: { 'Content-Type': 'application/json', 'Accept':'application/json' },
              body: JSON.stringify({ name: openTopic})
            };
            /* 
            const a = await fetch('/get-topic', requestOptions)
              .then(response => {return response.json()})
              .then(res => {return Array.from(res)})
              .catch(error => console.log(error));

            console.log("In Topic View", a);

            setList(a);*/
        }

        getList();
    }, [openTopic]);

    const removeListItem = (id) => {
      const newList = [...list];
      newList.splice(newList.indexOf(e => e.id !== id), 1);
      setList(newList);
    }

    return (
        <>
          <ul className='topic-view-container'>
              {list.map(pair => {
                  return (
                    <li key={pair.id}>
                      <div id='topic-source'>{pair.source}</div>
                      <div id='topic-translation'>{pair.translation}</div>
                      <button id='topic-delete-btn' onClick={() => {removeListItem(pair.id)}}></button>
                    </li>
                  );
              })}
          </ul>
        </>
    );
}


export default TopicView;