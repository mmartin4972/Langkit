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
          <button id='flip-source-button' onClick={() => props.flipSourceOrTranslations(true)}>Flip</button>
          <button id='flip-translation-button' onClick={() => props.flipSourceOrTranslations(false)}>Flip</button>
          <ul className='topic-view-container'>
              {props.pairs.map(pair => {
                if (!pair.sHidden && !pair.tHidden) {
                  console.log("Rendering what you shoud")
                  return (
                    <li key={pair.id}>
                      <button id='pair-source' onClick={() => {props.hideOrRevealTile(pair.id, true)}}>{pair.source}</button>
                      <button id='pair-translation' onClick={() => {props.hideOrRevealTile(pair.id, false)}}>{pair.translation}</button>
                      <button 
                        id='pair-delete-btn' 
                        onClick={() => {props.deletePair(pair.id)}}>
                      </button>
                    </li>
                  );
                }
                else if (pair.sHidden && !pair.tHidden) {
                  return (
                    <li key={pair.id}>
                      <button id='pair-source-hidden' onClick={() => {props.hideOrRevealTile(pair.id, true)}}>{pair.source}</button>
                      <button id='pair-translation' onClick={() => {props.hideOrRevealTile(pair.id, false)}}>{pair.translation}</button>
                      <button 
                        id='pair-delete-btn' 
                        onClick={() => {props.deletePair(pair.id)}}>
                      </button>
                    </li>
                  );
                }
                else if (!pair.sHidden && pair.tHidden) {
                  return (
                    <li key={pair.id}>
                      <button id='pair-source' onClick={() => {props.hideOrRevealTile(pair.id, true)}}>{pair.source}</button>
                      <button id='pair-translation-hidden' onClick={() => {props.hideOrRevealTile(pair.id, false)}}>{pair.translation}</button>
                      <button 
                        id='pair-delete-btn' 
                        onClick={() => {props.deletePair(pair.id)}}>
                      </button>
                    </li>
                  );
                }
                else {
                  return (
                    <li key={pair.id}>
                      <button id='pair-source-hidden' onClick={() => {props.hideOrRevealTile(pair.id, true)}}>{pair.source}</button>
                      <button id='pair-translation-hidden' onClick={() => {props.hideOrRevealTile(pair.id, false)}}>{pair.translation}</button>
                      <button 
                        id='pair-delete-btn' 
                        onClick={() => {props.deletePair(pair.id)}}>
                      </button>
                    </li>
                  );
                }
              })
            }
          </ul>
        </>
    );
}


export default TopicView;