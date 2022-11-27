import React, { useEffect, useState } from 'react';
import '../styles/styles';

function TopicListView () {
    const [list, setList] = useState([]);

    useEffect(() => {
        const getList = async () => {
            const requestOptions = {
              method: 'GET',
              headers: { 'Content-Type': 'application/json', 'Accept':'application/json' },
              body: JSON.stringify({})
            };
          
            const a = await fetch('/get-topics', requestOptions)
                .then(response => {return response.json()})
                .then(res => {return Array.from(res)})
                .catch(error => console.log(error));
            
            console.log("In Topic List", a);

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
          <ul className='topic-list-container'>
              {list.map(topic => {
                  return (
                    <li key={topic.id}>
                      <div id='topic-name'>{topic.name}</div>
                      <div id='topic-sourceLang'>{topic.sourceLang}</div>
                      <div id='topic-targetLang'>{topic.targetLang}</div>
                      <button id='topic-delete-btn' onClick={() => {removeListItem(topic.id)}}></button>
                    </li>
                  );
              })}
          </ul>
        </>
    );
}


export default TopicListView;