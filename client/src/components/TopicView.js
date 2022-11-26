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
              body: JSON.stringify({ username: 'Carson' , topic})
            };
          
            const a = await fetch('/get-topic', requestOptions)
              .then(response => {return response.json()})
              .then(res => {return Array.from(res)})
              .catch(error => console.log(error));

            setList(a);
        }

        getList();
    }, []);

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
                      <div id='topic-sourceLang'>{pair.source}</div>
                      <div id='topic-targetLang'>{pair.target}</div>
                      <button id='topic-delete-btn' onClick={() => {removeListItem(pair.id)}}></button>
                    </li>
                  );
              })}
          </ul>
        </>
    );
}


export default TopicView;