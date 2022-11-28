import '../styles/styles'

function GenerationWindow (props) {
    return (
        <>
            <div className="grid-ctr">
                <div className="basic-grid" id="generated-vocab">
                    {props.pairs.map(pair => {
                            return (
                                <button onClick={() => props.addPair(pair.source, pair.translation)}>
                                    <div id='src'>{pair.source}</div>
                                    <div id='mid'></div>
                                    <div id='trn'>{pair.translation}</div>
                                </button>
                            );
                        })
                    }
                </div>
            </div>
        </>
    );
}


export default GenerationWindow;