import '../styles/styles';

function TopicView (props) {
    return (
        <>
        <div className='topic-name-box'>
              <input 
                type="text" id='topic-name-edit-box' 
                className='topic-name-edit' 
                value={props.selectedTopicName}
                onChange={() => props.changeTopicNameBoxValue()}
                />
        </div>
          <ul className='topic-view-container'>
              {props.pairs.map(pair => {
                  return (
                    <li key={pair.id}>
                      <div id='pair-source'>{pair.source}</div>
                      <div id='pair-translation'>{pair.translation}</div>
                      <button 
                        id='pair-delete-btn' 
                        onClick={() => {props.deletePair(pair.id)}}>
                      </button>
                    </li>
                  );
              })}
          </ul>
        </>
    );
}


export default TopicView;