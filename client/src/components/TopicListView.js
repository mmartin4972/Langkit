import '../styles/styles';

function TopicListView (props) {
    return (
        <>
          <ul className='topic-list-container'>
              {props.topics.map(topic => {
                if (props.selectedTopic === topic.id) {
                  return (
                    <li key={topic.id} id='selected'>
                      <button id='topic-name' onClick={() => props.setSelectedTopic(topic.id)}>{topic.name}</button>
                      <div id='topic-sourceLang'>{topic.sourceLang}</div>
                      <div id='topic-targetLang'>{topic.targetLang}</div>
                      <button id='topic-delete-btn' onClick={() => {props.deleteTopic(topic.id)}}></button>
                    </li>
                  );
                }
                else {
                  return (
                    <li key={topic.id}>
                      <button id='topic-name' onClick={() => props.setSelectedTopic(topic.id)}>{topic.name}</button>
                      <div id='topic-sourceLang'>{topic.sourceLang}</div>
                      <div id='topic-targetLang'>{topic.targetLang}</div>
                      <button id='topic-delete-btn' onClick={() => {props.deleteTopic(topic.id)}}></button>
                    </li>
                  );
                }
              })}
          </ul>
        </>
    );
}


export default TopicListView;