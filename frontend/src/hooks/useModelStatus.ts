import {useEffect,useState} from 'react';
import {getStatus} from '../services/api';
import type {ModelStatus} from '../types';
export function useModelStatus(){const [status,setStatus]=useState<ModelStatus|null>(null);const [error,setError]=useState('');
 const refresh=()=>{getStatus().then(s=>{setStatus(s);setError('')}).catch(e=>{setStatus(null);setError(e instanceof Error?e.message:String(e))})};
 useEffect(()=>{refresh()},[]);return {status,error,refresh};}
