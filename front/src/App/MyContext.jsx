import React from 'react';
// import axios from 'axios';
import { useLocalStorage, localFunctions } from './useLocalStorage';
import { reducer, functions } from './reducer';
import { useReducer } from './useReducer';
import { Link, useParams, useNavigate } from 'react-router-dom';
import { Icons } from './Icons';
import Swal from 'sweetalert2';
import withReactContent from 'sweetalert2-react-content';
import { helper as hp } from './core/helper';

const MySwal = withReactContent(Swal);

const AllContext = React.createContext();

function MyContext(props){
    let init;
    try {
        init = from_init;
    }
    catch (error) {
        init = {};
    }

    const initialState = {
        classNames: {
            generalStyles: 'bg-white text-black',
        },
        init
    }

    const [s, dispatch] = useReducer({ reducer, initialState });
    const f = new functions(dispatch, s);

    const localInitialState = {
        theme: 'black',
    }
    // localStorage.removeItem('localStatev2');
    const [ls, localDispatch] = useLocalStorage('localState', localInitialState, f);
    const lf = new localFunctions(localDispatch, ls, s, f, dispatch);


    return (
        <AllContext.Provider
            value={{
                s, f,
                ls, lf, Icons, hp, 
                Link, useParams, useNavigate,
                MySwal,
            }}>
            {props.children}
        </AllContext.Provider>
    );
}


export { MyContext, AllContext };
