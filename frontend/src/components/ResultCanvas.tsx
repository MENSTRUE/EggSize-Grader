import {useEffect,useRef} from 'react';
import type {Prediction} from '../types';
const tones:Record<string,string>={large:'#5576e8',medium:'#11ad8c',small:'#e99a49'};
export function ResultCanvas({image,prediction}:{image:string;prediction:Prediction|null}){
 const ref=useRef<HTMLCanvasElement>(null);
 useEffect(()=>{if(!image)return;const img=new Image();img.onload=()=>{const c=ref.current;if(!c)return;const ctx=c.getContext('2d');if(!ctx)return;c.width=img.naturalWidth;c.height=img.naturalHeight;ctx.drawImage(img,0,0);
 if(prediction){const scale=c.width/Math.max(prediction.image_width,1);const sy=c.height/Math.max(prediction.image_height,1);const size=Math.max(2,Math.round(c.width/320));ctx.font=`bold ${Math.max(14,Math.round(c.width/42))}px Inter,Arial`;
 for(const d of prediction.detections){const [x1,y1,x2,y2]=d.box_xyxy;ctx.strokeStyle=tones[d.label]||'#fff';ctx.lineWidth=size*2;ctx.strokeRect(x1*scale,y1*sy,(x2-x1)*scale,(y2-y1)*sy);const label=`${d.label} ${(d.confidence*100).toFixed(0)}%`;const tw=ctx.measureText(label).width+16;const top=Math.max(0,y1*sy-30);ctx.fillStyle=tones[d.label]||'#111';ctx.fillRect(x1*scale,top,tw,30);ctx.fillStyle='#fff';ctx.fillText(label,x1*scale+8,top+22);}}
 };img.src=image;},[image,prediction]);
 return <canvas ref={ref} className="image-canvas" role="img" aria-label="Uploaded image with optional model detection boxes"/>;
}
