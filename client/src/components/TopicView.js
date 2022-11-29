import React, { useEffect, useState } from 'react';
import '../styles/styles';

function TopicView (props) {
    /*
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

            setList(a);
            const tempList = [
                {id: 0, source: 'Apple', translation: 'Manzana'},
                {id: 0, source: 'Plum', translation: 'Oleveda'},
                {id: 0, source: 'Banana', translation: 'Platana'},
                {id: 0, source: 'Togepi is in front of me and looks nice', translation: 'Togepi es en el frente de yo, y mira bueno'},
                {id: 0, source: 'Plum', translation: 'Oleveda'},
                {id: 0, source: 'Banana', translation: 'Platana'},
                {id: 0, source: 'Apple', translation: 'Manzana'},
                {id: 0, source: 'Plum', translation: 'Oleveda'},
                {id: 0, source: 'Banana', translation: 'Platana'}
            ];
            setList(tempList);
        }

        getList();
    }, []);

    const removeListItem = (id) => {
      const newList = [...list];
      newList.splice(newList.indexOf(e => e.id !== id), 1);
      setList(newList);
    }
  */
    return (
        <>
        <div className='topic-name-box'>
              <input type="text" id='topic-name-edit-box' className='topic-name-edit' defaultValue={props.selectedTopicName}/>
        </div>
          <ul className='topic-view-container'>
              {props.pairs.map(pair => {
                  return (
                    <li key={pair.id}>
                      <div id='pair-source'>{pair.source}</div>
                      <div id='pair-translation'>{pair.translation}</div>
                      <button id='pair-delete-btn' onClick={() => {props.deletePair(props.selectedTopicId, pair.id)}}></button>
                    </li>
                  );
              })}
          </ul>
        </>
    );
}


export default TopicView;